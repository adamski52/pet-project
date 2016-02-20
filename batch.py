import os
os.environ['DJANGO_SETTINGS_MODULE']='storybook.settings'
import sys, django, getopt
django.setup()

from datetime import datetime
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

from api.user.models import UserProfile
from api.invite.models import Invite
from api.dog.models import Dog


"""
oh hi.  looks best in sublime with the code viewer.



                                                                                      
                               .##+'+#@   :+###                                       
                             #@@@@@@@@@@@@@@@@@@#'''                                  
                           `#@@@@@@@@@@@@@@@@@@@@@@@@@                                
                        `#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+                              
                    ` ,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@,                          
                      @#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                        
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                       
                 `:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                 ,@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`                     
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
               ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;                    
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`                   
              .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'                   
             ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@`                  
          `  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                 
          `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
         ;@@@@@@@@@@@@@@@@@@#@@@@@@#@+.'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
        #@@@@@@@@@@@@@@@@@@@@@@@@#.       #@@@@@@@@@@@@@@@@@@@@@@@@@@@                
      `@#@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@@@@@@@@@`               
       @@@@@@@@@@@@@@@@@@###,               `+@@@@@@@@@@@@@@@@@@@@@@@@;`              
       @@@@@@@@@@@@@@@@@@@#                    @@@@@@@@@@@@@@@@@@@@@@@@               
       @@@@@@@@@@@@@@@@@@`                     @@@@@@@@@@@@@@@@@@@@@@@@               
       @@@@@@@@@@@@@@@                         @@@@@@@@@@@@@@@@@@@@@@@@`              
       @@@@@@@@@#.                             @@@@@@@@@@@@@@@@@@@@@@@@,              
       @@@@@@@@@                               @@@@@@@@@@@@@@@@@@@@@@@@;              
       @@@@@@@#                                @@@@@@@@@@@@@@@@@@@@@@@@@              
        +#@@#@                                 @@@@@@@@@@@@@@@@@@@@@@@@@              
         #@@@+              `                  ,@@@@@@@@@@@@@@@@@@@@@@@@              
          @@@               ;                    @@@@@@@@@@@@@@@@@@@@@@@              
          .@#           :@;                       @@@@@@@@@@@@@@@@@@@@@@              
           @#     ,#  ` ;@'                        @@@@@@@@@@@@@@@@@####              
          @@#   .@    ''      `                   ` @#@@@@@@@@@@@# `   .,             
         :@@`  #  ` ,,   `@@@;::                    '#@@@@@@@@@@@` @#++',             
          @@  @   ``  `  @@@@#@@@.   `               @@@@@@@@@@@+ @     :'`           
          @@  .` ,@@  ` @@@@@@@@@@@@@@@.`            `@@@@@@@@@@ ``     @@            
         .#@    #@@. , ,@@@@@@@@@@@@@@@@@:            @@@@@@#@#  ;      ;'            
          :@   @@@@. .    ,,,@@@@@@@@@@@@#+`          @@@@@@#@` ``       ``           
         `.#  @@@@@ : `        @@@@@@@@@@@#@@`        ;@@@@@@            @.           
           .`@@@@@` '`#               `:@+:           `@@@@@`      ` `    `           
            @@@@@'   .#                ` . @           @@@@#     #':   `  `           
         ``#@@@#'                       `.#           `@@#@`     @     +# `           
           @@@@@               ;; ;@`.  @  ';`        `#@@@      +     @#,            
          @@@@@@@+    `   ,    `@@@@@@@ @#`                            @#;            
          @@@@#`   #. #   @`  :@@@'`    '#:`                    #      ##;            
          @@@@  `    @ `  @`   @`     `                         `, `   `';            
          @@@     ````'@   `         '`                          @    #,`;            
          :@;   #@@@@@## `     +`  ;'                            @   `.+ '            
           @   @@@#';'#'       ` ``                              #  ' `  '            
           @  @@@     #+                                         #,,    `@            
           ..#+@     : @                                         @:     `             
            ,'+    '+ +@                                                @             
             @:,##'  + .                                               ,              
            `# .    @ `                                                #`             
             +#    `` ;       `                                     ` @               
             '     #  @       `;#,``',                           ` `@@@               
             @    :   .        ` `,   @                          @,` @@               
            ``    +  #            @    #                         @  `@@               
            +    ,   '           `@    `'                        @  '@@               
            @    @  @;           :       #       `               @  @@'               
            #    #  ,@     :;. `````      @      '               @  @@.               
            '    :  :`    ' `     ``       +     @               @  @@`               
            +    ,` # #,                   , '   @               @  @@                
            +    `.  ``                     ' ,  :               @. @@                
             .    ;             ,#@@@#@'    @ @  `               #``@@                
             #`  '    `     .@'`  :@@@@@@@. : @  `                .,@@                
              `  +       '#     @@@@@@@@@@#,` @  `                `:@@                
              @  ;     #:   `@@@#@# ; ' @`@#  @  `                .,@                 
              ``  ` ``;  `'@@@ @`,` , ' @;@;  @  +                .,@                 
               @  +  @`@@@@; . '``` @;@@@@@# `@  +                ..                  
                , :  #`@#, '`;`` :@@@@@@#@@+  @ `                 ..                  
                #  @ .`@#':;  `'@@@@@@@@@@'`  @ ;                 .`                  
               ``+ `#` @@#;#@#a2m@@@@@'@#@ @   @ @                 .`                  
                 .   @ '`@@@@@@@#@#`, +#  `   @ ;                 .                   
                  ; ` #`.;@@@@@#,`, @#   @    +                   .                   
                   @   `+ .#@@.  +@,    +     :;                 `  .                 
                    @  ' @  '''',      @     . @                 #  :                 
                     +  '`.       ` `#`      @ `               `@   +                 
                     .` : :#   `'@@;         '`                :    @                 
                    ``:  '  `               + @                ;    @                 
                       @ + `              `,` ;               #     ;,                
                        :``                . .              `@      `+                
                        ; #               ;  @              `         .               
                         ,@                                 @`        @               
                         :                                  `         +               
                         ;                                 `          `               
                         '                   `                         ;              
                         +                `@                          `@'             
                         +                +                           `, #            
                          ,              '`                            `' +           
                          #             #                               @ .           
                          `@`         ;;                                #  #          
                            `@.`   `@,                                  '@ `@         
                            ;  @@@:                                     `.   #`       
                            ;,`` #                                       @'    @      
                           +  #   @                                       @     #``   
                         ``.  ;    @                                     `@   ` `,@   
                          @`    `                                         @       ``  
                         ,     @    `                                     #        @  
                         #`    .                                          #      ` :  
                        `       #                                         ,           
                        @        #`                                       `         ` 
                                                                         .            
                                                                         @            
                                                                         @            
                                                                                      


                                                                                                    
                                                                                                    
                                    ```````````````                                                 
                  ``..-::/+++osssyyyyyyyyyyyyyyyyyyysssssoo++//:-..``                               
         `.-:/+ossyyhhhhhyysoo++//:---...```````` ````````...--:://+++++//:-.``                     
   .:/osyyhhhhhyys+//:-.```                                             ``.-::////:-``              
   :hhhyyso/:-.`                                                                  `.:::::-``        
    //-``                                                                               ``--.       
                 /:/`                                                                               
                 o:+-/-//-/:/:/-:/-//-/:`                                                           
      `-+oooo/.  o``.:-/-/o.+/.///-/+-/+`       .+++++++++-      /++:                               
     .sho:--/sh+`-  `. --`//+.``:-`--.:-        .yhhysssss:     `yhh+                               
     oho`    .yh-    ``   `.`   ``        ```   -hhh/         ` `yhho    ``           ``            
     sh+     `yh:oy+osyyo.  .+ssoss+``sy/ossys. .hhh+````` -syyyoyhh+ .oyyys+yyo` -oyyyyso-         
     sh+     `yh:sho` `/hs``sh:` `+ho`yh+```/ho -hhhyyyyyy.yhh+.:yhho`ohhs.-yhhs`:hhy:.:hhy.        
     sh+     `yh:sh-   `yy..yy:---/hy.yh.   -hs`-hhho::::--hyh- `yhh+`yhh+  ohhs`ohhy+/+yhh/        
     sh+     `yh:sh-   `yy.-hy+//////.yh.   -hs`-hhh+     .hhh- `yhh+`yhh/  ohhs`ohhy//////-        
     /hs`    :hy.sh/   -hy``yy-   -+/`yh.   -hs`-hhh+.````.yhh/ .yhh+`shho``shhs`/hhy. -sss-        
     `+yy+//oyy: shs+//yy/  :yy//+yy:`yh.   -hs`-hhhhhhhhho+hhyosyhho -shhysyhhs``ohhyoyhy+-`       
       `-://:-`  sh-.::-`    `-:::-` `--`   `-. `---------. .:::..--. .-::.`+hhs`  `-:::-` .        
                 sh-                                                  /hhy:/yhy/                    
                 /+.                                                   ./++o+/.                     
                                                                                                    
                                                                                                    

                            ^ if i'm found dead, this is the reason

"""


def invites():
    pending_invites = Invite.objects.filter(
        processed = False).order_by("recipient_email")

    recipients = pending_invites.values("recipient_email").distinct()

    emails = {}

    for recipient in recipients:
        recipient_email = recipient["recipient_email"]
        invites = pending_invites.filter(
            recipient_email = recipient_email)

        for invite in invites:
            id = str(invite.sender.id)
            emails.setdefault(recipient_email, {})
            emails[recipient_email].setdefault(id, {
                "invite_id": invite.id,
                "sender_first_name": invite.sender.first_name,
                "sender_last_name": invite.sender.last_name,
                "sender_email": invite.sender.email,
                "sender_dogs": []
            })

            emails[recipient_email][id]["sender_dogs"].append(invite.dog.name)

            

    # send em off
    for email in emails:
        context = list(emails[email].values())

        if len(context) > 1:
            text_message = render_to_string("templates/invites.txt", context)
            html_message = render_to_string("templates/invites.html", context)
        else:
            original_dogs = context[0]["sender_dogs"]
            sender_dogs = ""
            for dog in original_dogs[:-1]:
                sender_dogs += dog + ", " 
            sender_dogs += " and " + original_dogs[-1]

            sender_dogs = sender_dogs.replace(", and ", " and ")

            context[0]["sender_dogs"] = sender_dogs

            text_message = render_to_string("templates/invite.txt", context[0])
            html_message = render_to_string("templates/invite.html", context[0])

    

        send_mail(
            "Storybook Kennels Invite",
            text_message,
            "noreply@jonathanadamski.com",
            [email],
            html_message = html_message)

        print("Email sent to " + email + " with " + str(len(context)) + " invites.")




def main(argv):
    if "invites" in argv:
        invites()

    

if __name__ == "__main__":
    main(sys.argv[1:])


