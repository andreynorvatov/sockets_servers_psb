import socket
from time import sleep
import time
import csv
import re


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        time_res = str((time.perf_counter_ns() - start_time) / 1_000_000_000)
        # print(f'{time_res} sec')
        with open('time_metric.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow((time_res, 'sec', file_name))
        return res
    return wrapped


def parse_request(request):
    # request_params_dict = {'query': re.search(r"<query>(.+?)</query>", request).group(1)}
    request_params_dict = {'network_code': re.search(r"ns1:networkCode(.+?)</ns1:networkCode>", request).group(1)}
    return request_params_dict


def generate_headers():
    return 'HTTP/1.1 200 Ok\n\n'


def generate_body(request_params_dict):
    # query = request_params_dict['query']
    network_code = request_params_dict['network_code']

    first_string_body = '<?xml version="1.0" encoding="UTF-8"?>'
    second_string_body = '<soapenv:Body>'
    third_string_body = f'<query>networkCode is {network_code}</query>'
    fourth_string_body = '</soapenv:Body>'

    body = '\n'.join([first_string_body, second_string_body, third_string_body, fourth_string_body])
    return body


@time_of_function
def dump_txt(request):
    dump_dir = 'dumps/'
    time_stamp = str(time.time_ns())
    global file_name
    file_name = ''.join([dump_dir, time_stamp, '.txt'])
    file_data = request

    with open(file_name, 'w') as file:
        file.write(file_data)


def generate_response(request):
    request_params_dict = parse_request(request)
    headers = generate_headers()
    body = generate_body(request_params_dict)
    dump_txt(request)
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    file_cnt = 0
    while True:
        try:
            client_socket, addr = server_socket.accept()
            request = client_socket.recv(2048)

            response = generate_response(request.decode('utf-8'))

            client_socket.sendall(response)
            client_socket.close()
        except ConnectionResetError:
            print(f"Client suddenly closed, cannot send")

        if file_cnt < 5:
            file_cnt += 1
        else:
            file_cnt += 1
        print(file_cnt)


if __name__ == "__main__":
    print('Server started: 1234')
    HOST = '127.0.0.1'
    PORT = 1234
    dir = 'dumps'
    file_name = ''
    run()
