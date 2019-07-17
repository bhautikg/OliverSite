from mechanize import Browser, FormNotFoundError

import re

def checkbox_select(br):
    br.select_form(nr=0)
    for i in range(0, len(br.find_control(type="checkbox").items)):
        br.find_control(type="checkbox").items[i].selected =True

def do_processing(street1, street2, locationdetail, email, phone):
    br = Browser()
    #br.set_handle_robots(False)
    #br.set_handle_equiv(False)
    #br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open("https://secure.toronto.ca/webwizard/html/litter_bin_overflow.htm")

    br.select_form(nr=0)
    for i in range(0, len(br.find_control(type="checkbox").items)):
        br.find_control(type="checkbox").items[i].selected =True
    #checkbox_select(br)

    br.submit()

    #br.select_form(nr=0)
    #for i in range(0, len(br.find_control(type="checkbox").items)):
    #    br.find_control(type="checkbox").items[i].selected =True

    checkbox_select(br)

    br.submit()

    #br.select_form(nr=0)
    #for i in range(0, len(br.find_control(type="checkbox").items)):
    #    br.find_control(type="checkbox").items[i].selected =True
    checkbox_select(br)

    br["probCrossStreet1"] = street1
    br["probCrossStreet2"] = street2
    br["probLocationDetails"]= locationdetail
    br["ctctEmail"]= email
    br["ctctPhoneNumb"]= str(phone)

    br.submit()

    br.select_form(nr=0)

    br["additional_information"]="Reported by the waterfront BIA"

    br.submit()
    
    br.select_form(nr=0)

    response = br.submit()
    return (response.read())
