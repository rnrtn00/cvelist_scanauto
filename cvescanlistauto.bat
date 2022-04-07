@echo cve scan list automatically script 
pytest .\test_CVESCANKEYWORDResult_screen.py --html=./resultreport/report.html
python .\test_emailsend.py