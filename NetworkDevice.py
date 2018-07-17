class NetworkDevice:

    device_connection_parameters = ['device_type', 'ip', 'username', 'password', 'port', 'secret', 'verbose']
    device_connection_dic = {}

    def create_dictionary(*args):
        parameter_value_index = 0
        for parameter_index in NetworkDevice.device_connection_parameters:
            NetworkDevice.device_connection_dic[parameter_index] = args[1][parameter_value_index]
            parameter_value_index = parameter_value_index+1
        # print(NetworkDevice.device_connection_dic)
        pass

    def provide_dictionary():
        return NetworkDevice.device_connection_dic
