from .database_abstractions import getGeneralOrderObject


def slackMessage(order_id):
    blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "NEW GENERAL ORDER REQUEST \n\n Item Name: " 
                    + getGeneralOrderObject(order_id).item_name 
                    + "\n Requested Quantity: " + str(getGeneralOrderObject(order_id).quantity)
                    + "\n Ordered By: " + str(getGeneralOrderObject(order_id).student_name)
                    + "\n Order Date: " + str(getGeneralOrderObject(order_id).order_date)
                }
            },
            {
                "type": "actions",
                "block_id": "coskun" + ":" + str(order_id),
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Approve"
                        },
                        "action_id": "Approve",
                        "style": "primary",
                        "value": "aprrove_button"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Decline"
                        },
                        "action_id": "Decline",
                        "style": "danger",
                        "value": "decline_button"
                    }
                    
                ]
            }
        ]

    return blocks


def slackApprove(order_id):
    blocks = [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Item Name: " 
                    + str(getGeneralOrderObject(order_id).item_name)
                    + "\n Requested Quantity: " + str(getGeneralOrderObject(order_id).quantity)
                    + "\n Ordered By: " + str(getGeneralOrderObject(order_id).student_name)
                    + "\n Order Date: " + str(getGeneralOrderObject(order_id).order_date)
                    + "\n\n ORDER APPROVED"
                }
            }]
    return blocks

def slackDecline(order_id):
    blocks = [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Item Name: " 
                    + str(getGeneralOrderObject(order_id).item_name)
                    + "\n Requested Quantity: " + str(getGeneralOrderObject(order_id).quantity)
                    + "\n Ordered By: " + str(getGeneralOrderObject(order_id).student_name)
                    + "\n Order Date: " + str(getGeneralOrderObject(order_id).order_date)
                    + "\n\n ORDER DECLINED"
                }
            }]
    return blocks


def email(order_id):
    data = {
        'Messages': [
                {
                    "From": {
                        "Email": "coskunlab@gatech.edu",
                        "Name": "Coskun Lab"
                    },
                    "To": [
                        {
                            "Email": "joshptl313@gmail.com",
                            "Name": "Finance"
                        }
                    ],
                    "TemplateID": 2289447,
                    "TemplateLanguage": True,
                    "Subject": "New General Order Request",
                    "Variables": {
                        "item_name": str(getGeneralOrderObject(order_id).item_name) ,
                        "requested_quantity": str(getGeneralOrderObject(order_id).quantity),
                        "user_name": str(getGeneralOrderObject(order_id).student_name),
                        "order_date":  str(getGeneralOrderObject(order_id).order_date),
                        "order_id": str(order_id),
                    }
                }
            ]
    }
    return data