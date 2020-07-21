msg = {
    "en":{
        "AccountDeleted":"Your Account Is Deleted Please Contact Adminstration!",
        "AccountDeactivated":"Your Account Is Temperory Deactivated Please Contact Administration!"
    },
    "hi":{

    }
}

def get_language_based_msg(lang):
    return msg[lang]

def get_message_by_key(key,lang):
    msg_by_lang = get_language_based_msg(lang)
    return msg_by_lang[key]