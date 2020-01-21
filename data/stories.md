## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## job check
* job_check{"date":"today"}
  - date_form
  - form{"name": "date_form"}
  - form{"name": null}
  - slot{"date":"today"}
  - slot{"job_id":123}
  - slot{"address":"31 McKechnie Dr, Eight Mile Plains"}
  - slot{"description":"Very important job"}
* thanks
  - utter_ask_if_need_more_help

## job check + date
* job_check
  - utter_ask_date
* inform{"date":"today"}
  - date_form
  - form{"name": "date_form"}
  - form{"name": null}
  - slot{"date":"today"}
  - slot{"job_id":123}
  - slot{"address":"31 McKechnie Dr, Eight Mile Plains"}
  - slot{"description":"Very important job"}
* thanks
  - utter_ask_if_need_more_help

## next job
* next_job
  - action_next_job
  - slot{"job_id":123}
  - slot{"customer":"simPRO"}
  - slot{"address":"31 McKechnie Dr, Eight Mile Plains"}
  - slot{"description":"Very important job"}
* thanks
  - utter_ask_if_need_more_help
  
## locate tech
* locate_tech{"tech_name":"Simon Zyrianov"}
  - tech_form
  - form{"name": "tech_form"}
  - form{"name": null}
  - slot{"tech_name":"Simon Zyrianov"}
  - slot{"job_id":123}
  - slot{"customer":"simPRO"}
  - slot{"address":"31 McKechnie Dr, Eight Mile Plains"}
* thanks
  - utter_ask_if_need_more_help
  
## locate tech + tech name
* locate_tech
  - utter_ask_tech_name
* inform{"tech_name":"Simon Zyrianov"}
  - tech_form
  - form{"name": "tech_form"}
  - form{"name": null}
  - slot{"tech_name":"Simon Zyrianov"}
  - slot{"job_id":123}
  - slot{"customer":"simPRO"}
  - slot{"address":"31 McKechnie Dr, Eight Mile Plains"}
* thanks
  - utter_ask_if_need_more_help