# Web:

- Agent 95:
    - agents with older windows allowed
    - says about older windows → windows 95(from challenge name) → googled user agent for windows 95
    - `Mozilla/4.0 (compatible; MSIE 5.5; Windows 95; BCD2000)`
    - save and refresh gives `flag{user_agents_undercover}`
- Localghost:
    - extra addition of parts on scroll
    - check extra js
    - obfuscated
    - deobfuscate at jsnice.org
    - array has base64 string after `flag`
    - de base64-ing gives `JCTF{spoooooky_ghosts_in_storage}`