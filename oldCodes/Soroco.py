""""
bus ticket booking system - Eg Red bus

End user part 
Assuming buses are there


Search bus avilability - from location and to location and on a journey date
Search for type of bus - ac or no ac (feature)
after selecting the bus
seat avaialbility in the bus - no of person and seat number
book seat(s)


Controls
    1. SearchBus
        get
    2. FilterByFeature
        get
    3. BookSeats
        get
        post
        put
        delete


startPoint, endpoint, date, time

(
select busID, locations, Time  from Buses B
inner join operationPoint OP on OP.BusID = B.BusID
where time between time
date = date
statPoint= sp,
endPoint = ep
orderBy SequwnceNo
)
 - BusPpoints

(
select seat, startLoc, endLoc, busSeatID  from seatsBooked
where BusID = BusID
and status = 'Free'
)
 - seatBooked

for busID, sp, Ep, time in BusPoints:
    




DB:
    1. Buses
        a. Bus ID
        b. BusDetails
    2. operationPoint
        d. operationPointID
        a. Bus ID
        b. locations
        c. sequenceNo
        e. timeAtthislocation
    3. BusFeature
        a. BusFeatureID
        b. FeatureID - (Feature Table - id and feature name)
        c. BusID
    Del - luck - guj - bombay
    4. BusSeatBooked:
        a. BusID
        b. busSeatID
        c. startPoint
        d. EndPoint
        e. BookingID
        f. BookingStatus(blocked, booked)
        g. TimeStamp
    5. Booking:
        a. BookingID
        c. PaymentMode
        d. startingPoint
        e. dropPoint


WindowsService - 
    



50
45 - luck - guj
45 - guj - bombay








"""





