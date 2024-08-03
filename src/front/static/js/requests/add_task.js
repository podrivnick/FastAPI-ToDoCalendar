async function add_task_to_calendar(events) {
    const jsonAddTaskData = JSON.stringify(events)

    console.log(jsonAddTaskData)
    console.log(jsonAddTaskData.start_date)
    console.log(jsonAddTaskData.due_date)

    try {
        const response = await fetch(API_ADD_TASK, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: jsonAddTaskData,
        });

        if (response.ok) {
            window.location.reload();
            showNotification(ENTERED_TO_PROFILE)
            console.log('Registration successful', result);
        } else {
            console.error('Registration failed', result);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}