## What problem this application solving?
- Engineers often spend more time reconstructing their troubleshooting process than solving the actual issue. 
- During an investigation they focus on resolving the incident, not documenting each step. 
- By the time documentation is required, many details are forgotten. 
- AI Work Assistant captures speken resoining during troubleshooting and automatically converts it into structured technical documentation.
- Scenario: A support engineer might identify an issue, try out few workarounds steps to resolve it and one of which would fix the issue, but later would fail to document all the tries he did. 
- This app is a simple recording to document app where engineers while working on an issue start recording audio about what they are doing and then later the app would convert it into a documentation.

## Who would use it?
- Cloud Support enineers, CLoud Admin, Devops engineers, SRE, Developers, IT Admin. 

## What should version 1 be able to do?
- In the version one we are building this app to record and conver it to simple md document.
- Record microsophone
- Stop recording
- Generate transcript
- COnvert transcript to md
- Save MD file locally

## What should version 2 be able to do?
- Azure AI Speech
- Azure openAI
- Automatic summary
- Root cause detection
- Timeline generation
- Action items
- Lessons Learned

## What Azure services we would use?
- Azure OpenAI and Azure AI Speech services (Microsoft Foundry)
- Azure blob storage
- Azure key vault
- Azure app configurations
- Azure Monitor

## Future roadmap

- Voice commands
- AI suggestions
- Teams integration
- Jira integration
- ADO Integration
- Powershell history
- AZ CLI history
- Incident templates
- Export to Word, PDF
  