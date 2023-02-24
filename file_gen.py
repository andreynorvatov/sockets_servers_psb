import time
import csv


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        time_res = str((time.perf_counter_ns() - start_time) / 1_000_000_000)
        # print(f'{time_res} sec')
        with open('time_metric.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow((time_res, 'sec', file_cnt, file_name))
        return res

    return wrapped


file_name = ''


@time_of_function
def dump_txt():
    dump_dir = 'dumps/'
    # time_stamp = str(time.time())
    time_stamp = str(time.time_ns())
    global file_name
    file_name = ''.join([dump_dir, time_stamp, '.txt'])
    file_data = time_stamp
    time.sleep(0.000_000_000_001)
    # print(file_name)
    with open(file_name, 'w') as file:
        file.write(file_data)


file_cnt = 0
for i in range(10):
    file_cnt += 1
    dump_txt()

print(f'Generated: {file_cnt} files')
