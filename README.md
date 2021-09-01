# demonaterreminders
Reminds my friend to buy mods in D2 because he's bad and cant do it himself


### Prerequisites

Charlemagne bot [warmind.io](https://warmind.io/) must send daily updates in a discord text channel to give the bot vendor information.<br>
I could use Oauth, but I don't want to deal with that security.

### Commands

>registerme [braytech url]<br>
Sign into [braytech.org](https://braytech.org) and paste the url into the bot for it to remind you about daily mods<br>

>unregisterme <br>
Removes you from the list of people the bot will message


```javascript

{
    "token": "<bot token>",
    "apiKey": "<api key>",
    "Charlemagne-channel-id":"<api for channel of daily updates>",
    "usersToCheck": []
}

```
