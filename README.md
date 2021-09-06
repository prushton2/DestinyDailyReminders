# DestinyDailyReminders
Reminds people to buy mods in D2


### Prerequisites

Charlemagne bot [warmind.io](https://warmind.io/) must send daily updates in a discord text channel to give the bot vendor information.<br>
I could use Oauth, but I don't want to deal with that security.

### Commands

\>registerme [Bungie Name]<br>
Enter your bungie name (ex A_dmg04#4754) to sign up for daily reminders

\>unregisterme <br>
Removes you from the list of people the bot will message


```javascript

{
    "token": "<bot token>",
    "apiKey": "<api key>",
    "Charlemagne-channel-id":"<ID for channel of daily updates>",
    "usersToCheck": []
}

```

### TODO:
- Change the sign up command to allow someone to input their bungie name isntead of a scuffed url
