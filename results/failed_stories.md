## happy path 1 (/tmp/tmptzlpetku/f700ecae4a8e4b33b60e5357481a7db9_conversation_tests.md)
* greet: hello there!   <!-- predicted: Touched: hello there! -->
    - utter_greet   <!-- predicted: utter_Bag_confirmation -->
* mood_great: amazing   <!-- predicted: Greet: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->


## happy path 2 (/tmp/tmptzlpetku/f700ecae4a8e4b33b60e5357481a7db9_conversation_tests.md)
* greet: hello there!   <!-- predicted: Touched: hello there! -->
    - utter_greet   <!-- predicted: utter_Bag_confirmation -->
* mood_great: amazing   <!-- predicted: Greet: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->
* goodbye: bye-bye!   <!-- predicted: Order_a_bag: bye-bye! -->
    - utter_goodbye   <!-- predicted: action_custom_fallback -->


## sad path 1 (/tmp/tmptzlpetku/f700ecae4a8e4b33b60e5357481a7db9_conversation_tests.md)
* greet: hello   <!-- predicted: Touched: hello -->
    - utter_greet   <!-- predicted: action_custom_fallback -->
* mood_unhappy: not good   <!-- predicted: Order_of_fried_food: not good -->
    - utter_cheer_up   <!-- predicted: utter_Confirmation_of_order_completion -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: Greet: yes -->
    - utter_happy   <!-- predicted: utter_greet -->


## sad path 2 (/tmp/tmptzlpetku/f700ecae4a8e4b33b60e5357481a7db9_conversation_tests.md)
* greet: hello   <!-- predicted: Touched: hello -->
    - utter_greet   <!-- predicted: action_custom_fallback -->
* mood_unhappy: not good   <!-- predicted: Order_of_fried_food: not good -->
    - utter_cheer_up   <!-- predicted: utter_Confirmation_of_order_completion -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: Touched: not really -->
    - utter_goodbye   <!-- predicted: utter_Bag_confirmation -->


## sad path 3 (/tmp/tmptzlpetku/f700ecae4a8e4b33b60e5357481a7db9_conversation_tests.md)
* greet: hi   <!-- predicted: Greet: hi -->
    - utter_greet   <!-- predicted: action_custom_fallback -->
* mood_unhappy: very terrible   <!-- predicted: Order_cigarettes: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_Tobacco_touch_confirmation -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: Greet: no -->
    - utter_goodbye   <!-- predicted: utter_greet -->


## say goodbye (/tmp/tmptzlpetku/f700ecae4a8e4b33b60e5357481a7db9_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: Order_a_bag: bye-bye! -->
    - utter_goodbye   <!-- predicted: action_custom_fallback -->


## bot challenge (/tmp/tmptzlpetku/f700ecae4a8e4b33b60e5357481a7db9_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: Order_of_fried_food: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_Confirmation_of_order_completion -->


