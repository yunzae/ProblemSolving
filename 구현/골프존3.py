def solution(N, simulation_data):
    end_times = [0] * N
    total_waiting_time = 0

    for appointment in simulation_data:
        start_time, service_time = appointment
        min_end = 100000
        min_end_num = -1
        for i in range(N):
            if end_times[i] <= start_time:
                end_times[i] = start_time + service_time
                break
            if end_times[i] < min_end:
                min_end = end_times[i]
                min_end_num = i
            if i == (N - 1):
                total_waiting_time += min_end - start_time
                end_times[min_end_num] += service_time

    return total_waiting_time
