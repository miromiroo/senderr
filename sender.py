o
    Φb"?  ?                   @   s?  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dl
mZ d dlmZmZmZ d dl	mZmZmZmZ d dlmZ d dlmZmZmZmZmZmZmZ d dlmZmZm Z m!Z!m"Z"m#Z#m$Z$m%Z%m&Z& d dl'm(Z(m)Z) d d	l*m+Z+ d d
l,m-Z-m.Z. d dl/m0Z0m1Z1m2Z2 d dl3m4Z4 d dl5m6Z6m7Z7m8Z8m9Z9m:Z:m;Z;m<Z<m=Z= d dl>m?Z? d dl@Z@d dl5m<Z<mAZAm=Z= dZBdZCdZdZDdZEdZFejG?Hd?s?e?Id? ejG?Hd?s?eJdd? dZKddgZLg d?ZMdd? ZNe?  ejOZPejQZRejSZTejUZVejWZEejXZYeReTeVeEeYgZZdd? Z[d d!? Z\d"d#? Z]d$d%? Z^d&d'? Z_d(d)? Z`d*d+? Zad,d-? Zbd.d/? Zcd0d1? Zdd2d3? Zed4d5? Zfef?  dS )6?    N)?reader)?MINYEAR?datetime?	timedelta)?Fore?Back?Style?init)?TelegramClient)?	functions?typesr
   ?
connection?sync?utils?errors)	?InputPeerEmpty?UserStatusOffline?UserStatusRecently?UserStatusLastMonth?UserStatusLastWeek?PeerUser?PeerChannel?InputPeerChannel?InputPeerUser)?GetContactsRequest?DeleteContactsRequest)?DeletePhotosRequest)?GetDialogsRequest?ImportChatInviteRequest)?GetFullChannelRequest?JoinChannelRequest?InviteToChannelRequest)?SessionPasswordNeededError)?UsernameInvalidError?ChannelInvalidError?PhoneNumberBannedError?YouBlockedUserError?PeerFloodError?UserPrivacyRestrictedError?ChatWriteForbiddenError?UserAlreadyParticipantError)?StringSession)r)   ?UserBannedInChannelErrorr*   i?$ Z 7e14b38d250953c8c1e94fd7b2d63550z[1;31mz[1;32mz[1;36mz[1,35mz
./sessions?	phone.csv?w?
beast1.jpg?
beast2.jpg)r/   r0   z
beast3.jpgc                  C   s?   t ?  tdd??F} dd? t?| ?D ?}d}|D ]-}t?|?}|d7 }ttjt	j
 d|? ? ? td|? ?tt?}|?|? |??  t?  qd	}W d   ? n1 sQw   Y  t|ratjt	j d
 nd? ttjt	j d ? t?  d S )Nr-   ?rc                 S   s   g | ]}|d  ?qS )r   ? )?.0?rowr2   r2   ?%/storage/emulated/0/sender/sender2.py?
<listcomp>1   s    zlogin.<locals>.<listcomp>r   ?   zLogin ?	sessions/TzAll Number Login Done !zError!zPress Enter to back)?banner?open?csvr   r   ?parse_phone?printr   ?BRIGHTr   ZGREENr
   ?API_ID?HashID?start?
disconnect?RESET?YELLOW?input)?fZstr_listZpo?pphone?phone?client?doner2   r2   r5   ?login+   s"   

?
rK   c                   C   sN   t ?d? tdt? dt? dt? dt? dt? dt? dt? d	t? d
t? d?? d S )N?clear?
uw   
 ██████╗ ███████╗ █████╗ ███████╗████████╗u     
 ██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝un   
 ██████╔╝█████╗  ███████║███████╗   ██║    um   
 ██╔══██╗██╔══╝  ██╔══██║╚════██║   ██║   un   
 ██████╔╝███████╗██║  ██║███████║   ██║    ui   
 ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝   ╚═╝   z'
            Author: github.com/msy1717z#
            Developer : @Godmrunalz


)?os?systemr=   r1   r2   r2   r2   r5   r9   K   s(   
????????	?r9   c            	         ??   t d? t tjtj d ? tt? ?} tdd??}t|?}t	|?}| }d}||d  |d  }W d   ? n1 s9w   Y  t
?t? |?t?? }|?d? |d d ?? ???fd	d
?}|?  d S )N?"choose accout that are not limited?'Which Account You Want To Use?

Enter: r-   r1   r7   ?
config.ini?MRUNAL?SCRAP_GROUPc                     s?  t ???} td| ? ??? ?}|??  |?? sFz|?| ? |?| td?? td? |?| ? W n t	yE   td?}td? |j|d? Y nw ?}td? g }|j
|dd?}td	? td
ddd??J}tj|ddd?}|?g d?? |D ]0}|jr{|j}nd}|jr?|j}	nd}	|jr?|j}
nd}
|	d |
 ?? }|?||j|j|g? qrW d   ? n1 s?w   Y  tdt? ?? |?? j}td|? dt? ?? d}d}ttdt? ???}g }td
dd??=}tj|ddd?}t|d ? |D ]%}i }|d |d< t|d ?|d< t|d ?|d< |d |d< |?|? q?W d   ? n	1 ?sw   Y  d}ttd t? ???}|D ]?}|dk?rH|d dk?r@?q0|?|d ?}n|dk?rWt|d |d ?}ntd!t? ?? |??  t ?!?  z!td"|d ? |?"||?#|d ?? td#?#|?? t$?%|? W ?q0 t&?y?   td$? td#?#|?? t$?%|? Y ?q0 t'?y? } ztd%|? td&? td#?#|?? t$?%|? W Y d }~?q0d }~ww |??  td'? td(? d S ))Nr8   ?Enter code: ? ?Enter password: ??password?Fetching Members...F?Z
aggressive?Saving In file...?	msend.csvr.   ?UTF-8??encoding?,rM   ?Z	delimiterZlineterminator??usernamezuser idzaccess hash?name? ?Members scraped successfully.?Message was sending throuh ?(   ?   ?'Enter sleep time duration in messages :r   re   r7   ?id?   ?access_hash?   rf   zsend your messsage?Invalid Mode. Exiting.?Sending Message to:?Waiting {} seconds?\Getting Flood Error from telegram. Script is stopping now. Please try again after some time.?Error:?Trying to continue...? Done. Message sent to all users.?"
 Press enter to goto main menu...)(r   r<   r
   ?connect?is_user_authorized?send_code_request?sign_inrE   r=   r"   ?get_participantsr:   r;   ?writer?writerowre   ?
first_name?	last_name?striprm   ro   ?lg?get_me?ye?intr   ?next?append?str?get_input_entityr   rB   ?sys?exit?send_message?format?time?sleepr'   ?	Exception)rH   rI   rZ   ?target_group?all_participantsrF   r~   ?userre   r?   r?   rf   ?acc_name?SLEEP_TIME_2?SLEEP_TIME_1?
SLEEP_TIME?users?rowsr4   ?mode?message?receiver?e??api_hash?api_idrG   ?to_groupr2   r5   ?	sedmrunalr   s?   

???

??



??z messagesender.<locals>.sedmrunal?r=   r   r>   r   rD   r?   rE   r:   r   ?listr?   r@   ?configparserZConfigParser?read?	?Legend_devinput?read_obj?
csv_reader?list_of_rows?
row_number?
col_number?value?configr?   r2   r?   r5   ?messagesender\   s$   
?

\r?   c            	         rP   )NrQ   rR   r-   r1   r7   rS   rT   rU   c                     s?  t ???} td| ? ??? ?}|??  |?? sFz|?| ? |?| td?? td? |?| ? W n t	yE   td?}td? |j|d? Y nw ?}td? g }|j
|dd?}td	? td
ddd??J}tj|ddd?}|?g d?? |D ]0}|jr{|j}nd}|jr?|j}	nd}	|jr?|j}
nd}
|	d |
 ?? }|?||j|j|g? qrW d   ? n1 s?w   Y  tdt? ?? |?? j}td|? dt? ?? d}d}ttdt? ???}g }td
dd??=}tj|ddd?}t|d ? |D ]%}i }|d |d< t|d ?|d< t|d ?|d< |d |d< |?|? q?W d   ? n	1 ?sw   Y  td d!?}|?? }d}|}|D ]?}|dk?rJ|d dk?rB?q2|?|d ?}n|dk?rYt|d |d ?}ntd"t? ?? |??  t ?!?  z#td#|d ? |j"|d$|?#|d ?d%? td&?#|?? t$?%|? W ?q2 t&?y?   td'? td&?#|?? t$?%|? Y ?q2 t'?y? } ztd(|? td)? td&?#|?? t$?%|? W Y d }~?q2d }~ww |??  td*? td+? d S ),Nr8   rV   rW   rX   rY   r[   Fr\   r]   r^   r.   r_   r`   rb   rM   rc   rd   rg   rh   ri   rj   rk   rl   r   re   r7   rm   rn   ro   rp   rf   ?message.txt?rtrq   rr   r/   ?Zcaptionrs   rt   ru   rv   rw   rx   )(r   r<   r
   ry   rz   r{   r|   rE   r=   r"   r}   r:   r;   r~   r   re   r?   r?   r?   rm   ro   r?   r?   r?   r?   r   r?   r?   r?   r?   r   rB   r?   r?   ?	send_filer?   r?   r?   r'   r?   ?rH   rI   rZ   r?   r?   rF   r~   r?   re   r?   r?   rf   r?   r?   r?   r?   r?   r?   r4   ?textmsgr?   r?   r?   r?   r?   r2   r5   r?   ?   ??   

???

??



??zpcsender.<locals>.sedmrunalr?   r?   r2   r?   r5   ?pcsender?   ?$   
?

_r?   c            	         rP   )NrQ   rR   r-   r1   r7   rS   rT   rU   c                     ??  t ???} td| ? ??? ?}|??  |?? sFz|?| ? |?| td?? td? |?| ? W n t	yE   td?}td? |j|d? Y nw ?}td? g }|j
|dd?}td	? td
ddd??J}tj|ddd?}|?g d?? |D ]0}|jr{|j}nd}|jr?|j}	nd}	|jr?|j}
nd}
|	d |
 ?? }|?||j|j|g? qrW d   ? n1 s?w   Y  tdt? ?? |?? j}td|? dt? ?? d}d}ttdt? ???}g }td
dd??=}tj|ddd?}t|d ? |D ]%}i }|d |d< t|d ?|d< t|d ?|d< |d |d< |?|? q?W d   ? n	1 ?sw   Y  td d!?}|?? }d}|}|D ]?}|dk?rJ|d dk?rB?q2|?|d ?}n|dk?rYt|d |d ?}ntd"t? ?? |??  t ?!?  z#td#|d ? |j"|t#|?$|d ?d$? td%?$|?? t%?&|? W ?q2 t'?y?   td&? td%?$|?? t%?&|? Y ?q2 t(?y? } ztd'|? td(? td%?$|?? t%?&|? W Y d }~?q2d }~ww |??  td)? td*? d S ?+Nr8   rV   rW   rX   rY   r[   Fr\   r]   r^   r.   r_   r`   rb   rM   rc   rd   rg   rh   ri   rj   rk   rl   r   re   r7   rm   rn   ro   rp   rf   r?   r?   rq   rr   r?   rs   rt   ru   rv   rw   rx   ))r   r<   r
   ry   rz   r{   r|   rE   r=   r"   r}   r:   r;   r~   r   re   r?   r?   r?   rm   ro   r?   r?   r?   r?   r   r?   r?   r?   r?   r   rB   r?   r?   r?   ?photo2r?   r?   r?   r'   r?   r?   r?   r2   r5   r?   a  r?   zpcsender2.<locals>.sedmrunalr?   r?   r2   r?   r5   ?	pcsender2I  r?   r?   c            	         rP   )NrQ   rR   r-   r1   r7   rS   rT   rU   c                     r?   r?   ))r   r<   r
   ry   rz   r{   r|   rE   r=   r"   r}   r:   r;   r~   r   re   r?   r?   r?   rm   ro   r?   r?   r?   r?   r   r?   r?   r?   r?   r   rB   r?   r?   r?   ?photo3r?   r?   r?   r'   r?   r?   r?   r2   r5   r?   ?  r?   zpcsender3.<locals>.sedmrunalr?   r?   r2   r?   r5   ?	pcsender3?  r?   r?   c            
         ??   t d? t tjtj d ? tt? ?} tdd??}t|?}t	|?}| }d}||d  |d  }W d   ? n1 s9w   Y  t
?t? |?t?? }|?d? |d d }? ??fd	d
?}	|	?  d S )NrQ   rR   r-   r1   r7   rS   rT   rU   c                     s?  t ???} td| ? ??? ?}|??  |?? sFz|?| ? |?| td?? td? |?| ? W n t	yE   td?}td? |j|d? Y nw g }g }d }d}|t
|dt? |dd??}|?|j? |D ]}z|jd	kro|?|? W qb   Y qbtd
t ? d}	|D ]}
tt|	?d |
j ? |	d7 }	q?ttd??}td?}|dkr?t?  n	 tdd?}|?? }|}d}d}|?? D ]#}|jr?|j}z|d7 }|?||? t?|? W q?   |d7 }Y q?q?td|? d|? d?? d S )Nr8   rV   rW   rX   rY   ??   r   ?Zoffset_dateZ	offset_idZoffset_peer?limit?hashT?Your Joined Groups List?- r7   ?Enter Sleep time Duration?"PRESS Y to continoue else press N
?Nr?   r?   ?Done in ? chats, error in ? chat(s))r   r<   r
   ry   rz   r{   r|   rE   r=   r"   r   r   ?extend?chats?	megagroupr?   r?   r?   ?titler?   ?	main_menur:   r?   ?iter_dialogs?is_grouprm   r?   r?   r?   ?rH   rI   rZ   ?groupsr?   Z	last_dateZ
chunk_size?resultZchat?i?groupZmsy1717?sedrF   r?   ?msg?errJ   ?x?r?   r?   rG   r2   r5   r?   Q  sv   

??

?

?zgroupsender.<locals>.sedmrunalr?   ?
r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r2   r?   r5   ?groupsender;  ?$   
?

Br?   c            
         r?   )NrQ   rR   r-   r1   r7   rS   rT   rU   c                     ??  t ???} td| ? ??? ?}|??  |?? sFz|?| ? |?| td?? td? |?| ? W n t	yE   td?}td? |j|d? Y nw g }g }d }d}|t
|dt? |dd??}|?|j? |D ]}z|jd	kro|?|? W qb   Y qbtd
t ? d}	|D ]}
tt|	?d |
j ? |	d7 }	q?ttd??}td?}|dkr?t?  n	 tdd?}|?? }|}d}d}|?? D ]%}|jr?|j}z|d7 }|j|t|d? t?|? W q?   |d7 }Y q?q?td|? d|? d?? d S ?Nr8   rV   rW   rX   rY   r?   r   r?   Tr?   r?   r7   r?   r?   r?   r?   r?   r?   r?   r?   r?   )r   r<   r
   ry   rz   r{   r|   rE   r=   r"   r   r   r?   r?   r?   r?   r?   r?   r?   r?   r?   r:   r?   r?   r?   rm   r?   ?photor?   r?   r?   r?   r2   r5   r?   ?  ?v   

??

?

?zgroupsender1.<locals>.sedmrunalr?   r?   r2   r?   r5   ?groupsender1?  r?   r?   c            
         r?   )NrQ   rR   r-   r1   r7   rS   rT   rU   c                     r?   r?   )r   r<   r
   ry   rz   r{   r|   rE   r=   r"   r   r   r?   r?   r?   r?   r?   r?   r?   r?   r?   r:   r?   r?   r?   rm   r?   r?   r?   r?   r?   r?   r2   r5   r?     r?   zgroupsender2.<locals>.sedmrunalr?   r?   r2   r?   r5   ?groupsender2?  r?   r?   c            
         r?   )NrQ   rR   r-   r1   r7   rS   rT   rU   c                     r?   r?   )r   r<   r
   ry   rz   r{   r|   rE   r=   r"   r   r   r?   r?   r?   r?   r?   r?   r?   r?   r?   r:   r?   r?   r?   rm   r?   r?   r?   r?   r?   r?   r2   r5   r?   `  r?   zgroupsender3.<locals>.sedmrunalr?   r?   r2   r?   r5   ?groupsender3J  r?   r?   c                     s?   t d? t tjtj d ? tt? ?} tdd??}t|?}t	|?}| }d}||d  |d  }W d   ? n1 s9w   Y  t
?t? |?? ??fdd?}|?  d S )NrQ   rR   r-   r1   r7   c                     s?  t ???} td| ? ??? ?}|??  |?? sFz|?| ? |?| td?? td? |?| ? W n t	yE   td?}td? |j|d? Y nw td? t
dd?}d	}d	}d	}d	}|D ]c}z|d
7 }|t|?? td? t?d? W qY ty? }	 z|d
7 }t|	? W Y d }	~	qYd }	~	w ty? }
 z|d
7 }t|
? W Y d }
~
qYd }
~
w ty? } z|d
7 }t|? W Y d }~qYd }~ww td|? d|? d?? d S )Nr8   rV   rW   rX   rY   zCto join groups make grouo list in grouplist.txt and run this optionzgrouplist.txtr?   r   r7   zjoined Sucessfullyrn   r?   z chats , error in r?   )r   r<   r
   ry   rz   r{   r|   rE   r=   r"   r:   r    r?   r?   r,   r*   r?   )rH   rI   rZ   Zmrunalr?   rJ   ?trZpr?lineZpn?sr?   r?   r2   r5   r?   ?  sP   

?
????zjoiner.<locals>.sedmrunal?r=   r   r>   r   rD   r?   rE   r:   r   r?   r?   r@   ?r?   r?   r?   r?   r?   r?   r?   r?   r2   r?   r5   ?joiner?  s   
?
.r?   c                     s?   t d? t tjtj d ? tt? ?} tdd??}t|?}t	|?}| }d}||d  |d  }W d   ? n1 s9w   Y  t
?t? |?? ??fdd?}t d? |?  d S )	NrQ   rR   r-   r1   r7   c               	      s?   t ???} td| ? ??? ?}|??  |?? sFz|?| ? |?| td?? td? |?| ? W n t	yE   td?}td? |j|d? Y nw |?
tjjtjtdd?dtjd	d
?ddd??}d S )Nr8   rV   rW   rX   rY   r   )rm   ro   ZMrunalr?   )?dataT)ZcallZjoin_as?paramsZmutedZvideo_stopped)r   r<   r
   ry   rz   r{   r|   rE   r=   r"   Zinvoker   rH   ZJoinGroupCallRequestr   ZInputGroupCall?toZDataJSON)rH   rI   rZ   r?   r?   r2   r5   r?   	  s4   

?
???zvcjoiner.<locals>.sedmrunalZdoemr?   r?   r2   r?   r5   ?vcjoiner?  s    
?
r?   c                  C   s?  t ?  ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd t ? ttd	 t ? ttd
 t ? ttd t ? ttd??} | dkrjt?  d S | dkrst?  d S | dkr|t	?  d S | dkr?t
?  d S | dkr?t?  d S | dkr?t?  d S | dkr?t?  d S | dkr?t?  d S | dkr?t?  d S | dkr?t?  d S | dkr?t?  d S d S )NzChoose a Option:z            [1] Loginz            [2] Message Senderz0            [3] Message Sender[with photo 1 img]z0            [4] Message Sender[with photo 2 img]z0            [5] Message Sender[with photo 3 img]z0            [6] Group Sender                    z.            [7] Group Sender[with photo 1 img]z.            [8] Group Sender[with photo 2 img]z.            [9] Group Sender[with photo 3 img]z            [10] Group Joinerz
Enter your choice: r7   rn   rp   ?   ?   ?   ?   ?   ?	   ?
   ?   )r9   r=   r?   ?n?cyr?   rE   rK   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   )?ar2   r2   r5   r?   *  sH   










?r?   )g?
subprocessZrequestsr?   rN   ?re?	tracebackZrandomZloggingZtelethonZcoloramar;   Zjsonr?   r   r   r   r   r   r   r   r	   Ztelethon.syncr
   r   r   r   r   r   r   Ztelethon.tl.typesr   r   r   r   r   r   r   r   r   Ztelethon.tl.functions.contactsr   r   Ztelethon.tl.functions.photosr   Ztelethon.tl.functions.messagesr   r   Ztelethon.tl.functions.channelsr   r    r!   Ztelethon.errorsr"   Ztelethon.errors.rpcerrorlistr#   r$   r%   r&   r'   r(   r)   r*   Ztelethon.sessionsr+   Zasyncior,   r?   r@   Zgrr?   Zwi?path?exists?mkdirr:   r?   r?   r?   rK   rC   r?   ZLIGHTGREEN_EXr?   ZREDr1   ZWHITEr.   ZCYANrD   r?   Zcolorsr9   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r2   r2   r2   r5   ?<module>   sf   h $,(

tyyyZ[Z^I9
&