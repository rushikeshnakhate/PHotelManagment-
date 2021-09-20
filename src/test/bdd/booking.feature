Feature: HotelBooking

  Background:
    Given number of floors is 5 and rooms on each floor is 5

  Scenario: Room Sequence
    When hotel is created
    Then Room ara arranged in below sequence
      | RoomName | RoomStatus |
      | 1A       | Available  |
      | 1B       | Available  |
      | 1C       | Available  |
      | 1D       | Available  |
      | 1E       | Available  |
      | 2E       | Available  |
      | 2D       | Available  |
      | 2C       | Available  |
      | 2B       | Available  |
      | 2A       | Available  |


  Scenario: CheckIn
    Given Room status below
      | RoomName | RoomStatus |
      | 1A       | Available  |
    When Room is checkedIn
    Then Room status changes as below
      | RoomName | RoomStatus |
      | 1A       | Occupied   |

  Scenario: CheckOut
    Given Room status below
      | RoomName | RoomStatus |
      | 1A       | Occupied   |
    When Room is CheckedOut
    Then Room status changes as below
      | RoomName | RoomStatus |
      | 1A       | Vacant     |


  Scenario: Cleaning
    Given Room status below
      | RoomName | RoomStatus |
      | 1A       | Vacant     |
    When Room is Cleaned
    Then Room status changes as below
      | RoomName | RoomStatus |
      | 1A       | Available  |

  Scenario: Repairing Started
    Given Room status below
      | RoomName | RoomStatus |
      | 1A       | Vacant     |
    When Room is Repairing
    Then Room status changes as below
      | RoomName | RoomStatus |
      | 1A       | Repairing  |

#  Room under repair can only be vacant
#  which also means RepairingCompleted can be
#  only be done for under room under Repairing
  Scenario: Repaired
    Given Room status below
      | RoomName | RoomStatus |
      | 1A       | Repairing  |
    When Room is Repaired
    Then Room status changes as below
      | RoomName | RoomStatus |
      | 1A       | Vacant     |
