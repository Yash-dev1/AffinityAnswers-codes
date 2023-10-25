import requests
from urllib.parse import quote


def extr(address): # Defining a function to extract the pincode from the address itself
    addr = address.split() 
    for i in addr:
        if i.isdigit() and len(i) == 6:
            return i  # 6 digit pincode 
    return None  

# Desired function to test if the pincode is suitable/not
def checkpin(address):
    url_addr = quote(address) # making the address suitable for providing to URL
    # print(url_addr)

    url1 = f"https://api.postalpincode.in/pincode/{extr(address)}"  # requesting to the API for the pincode
    response = requests.get(url1)

    if response.status_code == 200: # if a successful response is generatd from the url
        rp = response.json() # accessing the dictionary formaat of the response
        if rp[0]['Status'] == 'Success':
            post_offices = rp[0]['PostOffice'] # Generating a list of post offices for the provided pincode
            # print(post_offices)
            for i in post_offices:
                if i['Name'] in url_addr:
                    return "Address Correct!"
        else:
            return "Ehhhnnn! Incorrect address!"
    return "Ehhhnnn! Incorrect address!"

def inp():
    inp1 = "30, Barpeta, Barpeta, Assam 781301" # sample input1 
    inp2 = "2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari (3rd Stage/0, Srinivasa Nagar, Bengaluru, Karnataka 560050" # smaple input2 with special characters in the address
    inp3 = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095" # sample input3 
    inp4 = "Colony, Bengaluru, Karnataka " # sample input4 input with no pincode
    print(checkpin(inp1))
    print(checkpin(inp2))
    print(checkpin(inp3))
    print(checkpin(inp4))

if __name__ == "__main__":
    inp()






