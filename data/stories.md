<!-- 揚げ物yes、タバコyes、袋yes -->
## Convini Story 1
* Request_for_payment
  - utter_Accounting_start
* Order_of_fried_food OR Agree
  - utter_Confirmation_of_order_completion
* Order_cigarettes
  - utter_Tobacco_touch_confirmation
* Touched OR Agree
  - utter_Bag_confirmation
* Order_a_bag OR Agree
  - utter_Check_if_the_bag_is_the_same
* Agree OR Refusal
  - utter_Accounting_confirmation
* Agree
  - utter_Say_thanks


<!-- 揚げ物yes、タバコyes、袋no -->
## Convini Story 2
* Request_for_payment
  - utter_Accounting_start
* Order_of_fried_food OR Agree
  - utter_Confirmation_of_order_completion
* Order_cigarettes
  - utter_Tobacco_touch_confirmation
* Touched OR Agree
  - utter_Bag_confirmation
* Refuse_the_bag OR Refusal
  - utter_Accounting_confirmation
* Agree
  - utter_Say_thanks


<!-- 揚げ物yes、タバコno、袋yes -->
## Convini Story 3
* Request_for_payment
  - utter_Accounting_start
* Order_of_fried_food OR Agree
  - utter_Confirmation_of_order_completion
* End_of_order OR Agree
  - utter_Bag_confirmation
* Order_a_bag OR Agree
  - utter_Check_if_the_bag_is_the_same
* Agree OR Refusal
  - utter_Accounting_confirmation
* Agree
  - utter_Say_thanks


<!-- 揚げ物yes、タバコno、袋no -->
## Convini Story 4
* Request_for_payment
  - utter_Accounting_start
* Order_of_fried_food OR Agree
  - utter_Confirmation_of_order_completion
* End_of_order OR Agree
  - utter_Bag_confirmation
* Refuse_the_bag OR Refusal
  - utter_Accounting_confirmation
* Agree
  - utter_Say_thanks



<!-- 揚げ物no、タバコyes、袋yes -->
## Convini Story 5
* Request_for_payment
  - utter_Accounting_start
* Refusal
  - utter_Confirmation_of_order_completion
* Order_cigarettes
  - utter_Tobacco_touch_confirmation
* Touched OR Agree
  - utter_Bag_confirmation
* Order_a_bag OR Agree
  - utter_Check_if_the_bag_is_the_same
* Agree OR Refusal
  - utter_Accounting_confirmation
* Agree
  - utter_Say_thanks


<!-- 揚げ物no、タバコyes、袋no -->
## Convini Story 6
* Request_for_payment
  - utter_Accounting_start
* Refusal
  - utter_Confirmation_of_order_completion
* Order_cigarettes
  - utter_Tobacco_touch_confirmation
* Touched OR Agree
  - utter_Bag_confirmation
* Refuse_the_bag OR Refusal
  - utter_Accounting_confirmation
* Agree
  - utter_Say_thanks


<!-- 揚げ物no、タバコno、袋yes -->
## Convini Story 7
* Request_for_payment
  - utter_Accounting_start
* Refusal
  - utter_Confirmation_of_order_completion
* End_of_order OR Agree
  - utter_Bag_confirmation
* Order_a_bag OR Agree
  - utter_Check_if_the_bag_is_the_same
* Agree OR Refusal
  - utter_Accounting_confirmation
* Agree
  - utter_Say_thanks


<!-- 揚げ物no、タバコno、袋no -->
## Convini Story 8
* Request_for_payment
  - utter_Accounting_start
* Refusal
  - utter_Confirmation_of_order_completion
* End_of_order OR Agree
  - utter_Bag_confirmation
* Refuse_the_bag OR Refusal
  - utter_Accounting_confirmation
* Agree
  - utter_Say_thanks


<!-- お礼 -->
## Thanks Story
* Thank
  - utter_thanks


<!-- あいさつ -->
## Greet Story
* Greet
  - utter_greet

