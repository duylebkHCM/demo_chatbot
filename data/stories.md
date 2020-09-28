## First contact
* Request_for_payment
  - Accounting_start

## Fried food story
* Order_of_fried_food
  - Confirmation_of_order_completion
* Refusal
  - Confirmation_of_order_completion

## Tobacco story
* Order_cigarettes
  - Tobacco_touch_confirmation
* Touched
  - Bag_confirmation
* End_of_order
  - Bag_confirmation

## Bag confirmation story
* Order_a_bag
  - Check_if_the_bag_is_the_same
* Agree
  - Accounting_confirmation
* Refuse_the_bag
  - Accounting_confirmation

## ending
* Agree
  - Say_thanks

