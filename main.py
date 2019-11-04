import csv
from getMetricsData import get_final_list


def writeCSV():
    """
    This function writes the output to a CSV file.
    :return:
    """
    final_list = get_final_list()
    path_to_csv_File = 'system_metrics.csv'

    csv_file = open(path_to_csv_File, 'w+', newline='', encoding="utf8")
    csv_file_writer = csv.writer(csv_file, delimiter=',')

    csv_file_writer.writerow(['Subscription', 'Resource', 'MetricType',
                              'Timestamp', 'Unit', 'Minimum', 'Maximum', 'Average'])

    for item in final_list:
        csv_file_writer.writerow([item['subscription'], item['resource'], item['metricType'], item['timestamp'],
                                 item['unit'], item['minimum'], item['maximum'], item['average']])

    print('Output written successfully!!')


if __name__ == '__main__':
    writeCSV()
