from netmiko import ConnectHandler
import NetworkDevice
import time
from netmiko import ssh_exception


def main():
    device_path = 'Data/network_device_list.txt'
    command_path = 'Data/commands.txt'
    output_path = 'Outputs/'
    unknown_devices_list = []
    command_list = []

    # gather all device connection parameters and put it into a list
    with open(device_path, 'r') as network_device_file:
        for index, line in enumerate(network_device_file):
            unknown_devices_list.append(line.split(' '))
    network_device_file.close()

    # gather all the commands and put it into a list
    with open(command_path, 'r') as command_file:
        for index, line in enumerate(command_file):
            command_list.append(line.splitlines())
    command_file.close()

    for connection_param in unknown_devices_list:
        device = NetworkDevice.NetworkDevice()
        device.create_dictionary(connection_param)
        try:
            net_connect = ConnectHandler(**NetworkDevice.NetworkDevice.provide_dictionary())
            net_connect.enable()
            time_now = time.strftime("%a_%d_%b_%Y_%H;%M;%S", time.gmtime())
            new_output_path = ''.join(
                output_path + connection_param[0] + '_' + connection_param[1] + '_' + time_now + '.txt')
            output_file = open(new_output_path, 'w')
            for command in command_list:
                output = net_connect.send_command(''.join(command))
                output_file.write('\n****************' + ' ' + ''.join(command) + ' ' + '****************\n')
                output_file.write(output)
                output_file.write('\n****************' + ' ' + 'END' + ' ' + '****************\n')
            net_connect.exit_enable_mode()
            output_file.close()
            net_connect.disconnect()
            print('successfully gathered command output from:', connection_param[0] + ' ' + connection_param[1])
        except ssh_exception.NetMikoTimeoutException as err:
            print(err)
            pass


if __name__ == '__main__':
    main()
