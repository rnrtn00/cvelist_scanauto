# Project : CVE Scanning Automation
## Purpose
Customer's request about the monitoring of some keywords' searching result in http://cve.mitre.org web site has occurred.
The web site is for managing SW vulnerability DB and operated by one of US government-affiliated institue.
The keywords have defied through the discussion with the customer. These keywords' searching is a kind of simple but repetitive task.
So I made this simple project to relieve the tedium.

## Used major technique
- Python 3
- Selenium
- Pytest

## Simple Diagram and Sequences
- Diagram


- Sequences
 - 1st. Keywords searching will be executed in the web site using pytest and selenium. If the keywords' search result are different compared to the last week result, the web page including the different result would be captured and inserted in the result.
 - 2nd. If the keywords searching has finished well, a draft result file format:XML is going to be converted to HTML.
 - 3rd. The converted HTML format result file will be archived with a css file prepared in advance for visibility.
 - 4th. The archived file will be sent to the target e-mail address. (End)

