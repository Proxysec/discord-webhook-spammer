import requests, sys, json, random, string
from colorama import Fore
from random import choices


def main():
    g = Fore.GREEN
    y = Fore.YELLOW
    R = Fore.RED
    w = Fore.WHITE
    c = Fore.CYAN
    print(f"{g}HAPPY HOLDAY {w}| {c}BY {R}N.. {g}<33\n")
    u = input(f"{c}Webhook {g}Token {R}: {w}")
    ifd = input(f"{c}Webhook {g}Channel {w}ID {R}: {w}")
    mess = input(f"{c}Message {g}Or {c}default {w}msg {R}: {w}")
   
    

    i = int(input(f"{c}Number {g}of {c}resends {R}: {w}"))
    
    
    val = 1
    while val <= i:
        if mess == "default":
            #codess = ('').join(random.choices(string.ascii_letters + string.digits, k=50))
            lag =  ':grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face: ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽:grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses:'
        Y = requests.get(f"https://discord.com/api/webhooks/{ifd}/{u}", timeout=8)
        parsethis = json.loads(Y.text)
        if Y.status_code == "404":
            print("Looks like a 404? weird")
            sys.exit()


        try:
            lol = parsethis['message']
            if lol == "Invalid Webhook Token":
                print("Could not find Webhook")
                return main()
            if lol == "Unknown Webhook":
                print("Could not find Webhook")
                return main()

        except:
            pass
        if mess == "default":
            lag = ':grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face: ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽:grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses:'
            
        else:
            lag = ''
        
        print(f"{c}SENT {w}to {R}{ifd} {w}| {c}Message {R}{mess} ")
        url = f"{Y.url}"
        Message = {
                "username": "system",
                "content": f"{mess}{lag}"
                
        }
                
                
                
                
        requests.post(url, data=Message)
        val += 1
        
        
        
    
    
main()

 
 
