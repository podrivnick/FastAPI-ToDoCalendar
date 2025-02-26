async function add_task_to_calendar(events) {
    const jsonAddTaskData = JSON.stringify(events)


    try {
        const response = await fetch(API_ADD_TASK, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: jsonAddTaskData,
        })
        .then(response => response.json())
            .then(data => {
                localStorage.setItem("events", JSON.stringify(data));
            })
    } catch (error) {
        console.error('Error:', error);
    }
}
