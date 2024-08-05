async function delete_task_from_calendar(events) {

    console.log(events)
    try {
        const response = await fetch(API_DELETE_TASK, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: events,
        })
        .then(response => response.json())
            .then(data => {
                console.log(data)
            })
    } catch (error) {
        console.error('Error:', error);
    }
}
