import time
import multiprocessing

pool_processors = multiprocessing.cpu_count()
file_chunk_size = 10 * 1024 * 1024  # 10MB

# IP range from RFC6890 - IP range for future use
# it does not conflict with https://github.com/bitcoin/bitcoin/blob/master/src/netbase.h
ip_range = "240.0.0.0/4"
ip_zones = '240.{}.0.0/16'

standard_image = 'simcoin/patched:v2'

network_name = 'simcoin-network'
prefix = 'simcoin-'
node_prefix = 'node-'
node_name = node_prefix + '{}.{}'
selfish_node_prefix = 'selfish-node-'
selfish_node_proxy_postfix = '-proxy'
selfish_node_name = selfish_node_prefix + '{}'
selfish_node_proxy_name = selfish_node_name + selfish_node_proxy_postfix

rpc_user = 'admin'
rpc_password = 'admin'
rpc_port = 18332
rpc_simulation_timeout = 0.25


def create_rpc_connection_string(ip):
    return 'http://{}:{}@{}:{}'.format(rpc_user, rpc_password, ip, rpc_port)


reference_node = 'node-0'

blocks_needed_to_make_coinbase_spendable = 100
max_in_mempool_ancestors = 25

log_prefix_timestamp = r'^([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6}) '
log_error_grep = 'grep -E -i "WARN|FATAL|ERROR|CRITICAL|EXCEPTION" {} || true'
log_time_format = '%Y-%m-%d %H:%M:%S.%f'
log_line_run_start = 'RUN START '
log_line_run_end = 'RUN END '

smallest_amount = 1
smallest_amount_btc = 0.00000001
transaction_fee = 1000

amount_of_system_snapshots = 500

bitcoin_log_file_name = '/debug.log'

data_dir = '../data/'

network_csv_file_name = 'network.csv'
ticks_csv_file_name = 'ticks.csv'
nodes_csv_file_name = 'nodes.csv'
args_csv_file_name = 'args.csv'

network_csv = data_dir + network_csv_file_name
ticks_csv = data_dir + ticks_csv_file_name
nodes_csv = data_dir + nodes_csv_file_name
args_csv = data_dir + args_csv_file_name

bitcoin_data_dir = '/data'
client_dir = bitcoin_data_dir + '/regtest'

report_file_name = 'report.Rmd'
multi_report_file_name = 'multi_report.Rmd'

multi_run_dir = '{}multi-run-{}'.format(data_dir, time.time())

log_file = data_dir + 'debug.log'
soft_link_to_run_dir = '{}last_run'.format(data_dir)
soft_link_to_multi_run_dir = '{}last_multi_run'.format(data_dir)
run_log = soft_link_to_run_dir + '/run.log'

analysed_tick_infos_file_name = 'analysed_tick_infos.csv'
step_times_csv_file_name = 'step_times.csv'
consensus_chain_csv_file_name = 'consensus_chain.csv'

postprocessing_dir = soft_link_to_run_dir + '/postprocessing/'
consensus_chain_csv = postprocessing_dir + consensus_chain_csv_file_name
general_infos_csv = postprocessing_dir + 'general_infos.csv'
log_errors_txt = postprocessing_dir + 'log_errors.txt'
analysed_ticks_csv = postprocessing_dir + 'analysed_ticks.csv'
