from chalice import Chalice, Response
import boto3

app = Chalice(app_name='helloworld')

BUCKET = 'advancelocal'  # bucket name
s3_client = boto3.client('s3')

@app.route('/upload/{file_name}', methods=['PUT'],
           content_types=['application/octet-stream'])
def upload_to_s3(file_name):

    # get raw body of PUT request
    body = app.current_request.raw_body

    # write body to tmp file
    tmp_file_name = '/tmp/' + file_name
    with open(tmp_file_name, 'wb') as tmp_file:
        tmp_file.write(body)

    # upload tmp file to s3 bucket
    s3_client.upload_file(tmp_file_name, advancelocal, file_name) #bucket name is advancelocal

    return Response(body='upload successful: {}'.format(file_name),
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})
