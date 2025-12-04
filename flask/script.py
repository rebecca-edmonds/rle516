import subprocess
import sys
from flask import Flask, render_template

    
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    df = pd.DataFrame({'enabled':[True, False],'code':["Y2025-abc", "Y2025-def"], "a":["x", "y"]})
    df['enabled'] = df['enabled'].apply(lambda x: '<input type="checkbox" name="one" value="one" checked>' if x else '<input type="checkbox" name="one" value="one" unchecked>')
    t = df.to_html(classes='data', escape=False, table_id="main_table")
    return render_template('index.html', tables=[t], titles=df.columns.values)
  
if __name__ == '__main__':
    app.run(debug=True)

