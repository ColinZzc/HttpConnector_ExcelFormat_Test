from flask import Flask, send_file, abort, Response  
import os  
  
app = Flask(__name__)  
  
@app.route('/EQ06.xlsx', methods=['GET'])  
def get_excel_file():  
    file_path = 'EQ06.xlsx'  # Replace with the actual path to your Excel file  
  
    # Check if the file exists  
    if not os.path.exists(file_path):  
        abort(404)  
  
    # Return the file  
    return send_file(file_path, as_attachment=True, download_name='EQ06.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  


def generate_chunks(file_path):  
    with open(file_path, 'rb') as f:  
        while True:  
            chunk = f.read(8192)  # Read the file in 8KB chunks  
            if not chunk:  
                break  
            yield chunk  
  
@app.route('/chunks/EQ06.xlsx', methods=['GET'])  
def get_chunks_excel_file():  
    file_path = 'EQ06.xlsx'  # Replace with the actual path to your Excel file  
  
    # Check if the file exists  
    if not os.path.exists(file_path):  
        abort(404)  
  
    # Stream the file in chunks  
    response = Response(generate_chunks(file_path), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
    response.headers['Content-Disposition'] = 'attachment; filename=EQ06.xlsx'  
    # response.headers['Transfer-Encoding'] = 'chunked'  # no need to set this header, Flask will automatically use chunked transfer encoding
    return response  


if __name__ == '__main__':  
    app.run(debug=True, host='0.0.0.0', port=5000)  