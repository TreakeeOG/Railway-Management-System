from db import get_connection, create_RMS

def create_user_table():
    create_RMS()
    con = get_connection()
    cur = con.cursor()
    cur.execute("USE RMS")
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            userID INT PRIMARY KEY,
            password VARCHAR(40) NOT NULL
        )
        """
    )
    con.commit()
    con.close()

def create_train_table():
    create_RMS()
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Train (
            TrainID INT PRIMARY KEY,
            Train_Name VARCHAR(30) NOT NULL,
            Source_Station VARCHAR(30) NOT NULL,
            Destination VARCHAR(30) NOT NULL
        )
        """
    )
    con.commit()
    con.close()

def create_passenger_table():
    create_RMS()
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Passenger (
            PassengerID INT PRIMARY KEY,
            Passenger_Name VARCHAR(30) NOT NULL,
            Age INT CHECK (Age > 0),
            Gender VARCHAR(10),
            Phone_Number BIGINT UNIQUE
        )
        """
    )
    con.commit()
    con.close()

def create_booking_table():
    create_RMS()
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Booking (
            PNR_No INT PRIMARY KEY,
            TrainID INT,
            PassengerID INT,
            Booking_Date DATE NOT NULL,
            Departure_Date DATE NOT NULL,
            Fare INT CHECK (Fare >= 0),
            FOREIGN KEY (TrainID) REFERENCES Train(TrainID),
            FOREIGN KEY (PassengerID) REFERENCES Passenger(PassengerID)
        )
        """
    )
    con.commit()
    con.close()

def create_cancellation_table():
    create_RMS()
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Cancellation (
            PNR_No INT,
            Cancellation_Date DATE NOT NULL,
            Refund_Amount INT CHECK (Refund_Amount >= 0),
            FOREIGN KEY (PNR_No) REFERENCES Booking(PNR_No)
        )
        """
    )
    con.commit()
    con.close()

def create_all_tables():

    create_RMS()
    create_user_table()
    create_train_table()
    create_passenger_table()
    create_booking_table()
    create_cancellation_table()


