Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975



**Test Cases**
Table 1. Summary of test cases for `buy_cheese` function in `shop.py`. 
| Test ID | Description                        | Inputs.     | Expected Output                             | Status |
| ------- | ---------------------------------- | ----------- | ------------------------------------------- | ------ |
| 01      | Buy cheese with insufficient gold. | "swiss 3"   | "Insufficient gold."                        | Pass   |
| 02      | Buy negative amount of cheese.     | "marble -2" | "Must purchase positive amount of cheese."  | Pass   |
| 03      | Buy multiple cheese of same type.  | "cheddar 3" | (30, (0, 3, 0))                             | Pass   |

Table 2. Summary of test cases for `change_cheese` function in `game.py`.
| Test ID | Description                        | Inputs.            | Expected Output    | Status |
| ------- | ---------------------------------- | ------------------ | ------------------ | ------ |
| 04      | Arm trap with available cheese.    | [("cheddar", 2)]   | (True, "cheddar"). | Pass   |
| 05      | Player enters invalid cheese name. | rock               | "No such cheese!"  | Pass   |
| 06      | Back after entering cheese name.   | cheddar back       | (False, None)      | Pass   |    | Pass   |
