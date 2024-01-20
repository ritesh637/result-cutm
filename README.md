# Welcome to CUTM Result Source Code !

Hello All ! Welcome to The CUTM Result Repository .

# How to Run !

- In Development :
  -- First of All Clone the Repo or Download the Zip via Github
  -- You need to have Python installed in your System .
  -- Go to the Project / Repo Folder
  -- Install All Requirements by Typing the Below Command . 👇

  > `pip install -r requirements.txt`

- Then start the Server by typing 👇
  > `python app.py`
- This will start the server at `http://localhost:5000`

## For Inserting Result Record into SQLite Database .

- Place All the Excel Sheets into Results Folder inside the Project Folder .
- Then, In the Project folder type 👇

  > python3 convert_tool.py run

- This will empty the earlier record and Dump the excel sheets into sqlite3 db .
- If You want to Experiment with convert_tool . Type 👇

  > python3 convert_tool.py

## Automate the Whole Process .

- I have Also written the Github actions CI to automate the whole process with Just git push command .
- You can Suggest more Features for this.

## Contribute

**Make a Pull Request or Open Issue for More Feature .**
Please Feel Free to Contact , If you Have Any Issue ! Will be Happy to Help You 😀

### Tech Used

- Python (Flask ) .
- SQLite3 DB .
- Bootstrap 4.4
- Heroku - For Hosting .
- Github Actions CI/CD for automation .

### Contributor

<a href="https://github.com/ashish-devv/Result-flask/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ashish-devv/Result-flask" />
</a>
