async function converting_event_obj(
        events_obj,
        eventTitle,
        eventTask,
        eventPriority,
    )
{
    // clone object, which contains events data
    let cloneEventsArrForRequest = await JSON.parse(JSON.stringify(events_obj))

    await cloneEventsArrForRequest.forEach(obj => {
        delete obj.events
    });

    let cleaned_events = cloneEventsArrForRequest[cloneEventsArrForRequest.length - 1]
    cleaned_events = {
        ...cleaned_events,
        title: eventTitle,
        task: eventTask,
        priority: eventPriority,
    };
    let num_priority = Number(cleaned_events.priority);

    if (isNaN(num_priority)) {
        throw new Error('Не удалось преобразовать значение в число');
    }

    cleaned_events.priority = num_priority;
    // format time to ISO format
    console.log(
            cleaned_events.day,
            cleaned_events.time_from,
            cleaned_events.month,
            cleaned_events.year,
    )
    const start_date = await
        formatDateTime
        (
            cleaned_events.day,
            cleaned_events.time_from,
            cleaned_events.month,
            cleaned_events.year,
        )
    const due_date = await
        formatDateTime
        (
            cleaned_events.day,
            cleaned_events.time_to,
            cleaned_events.month,
            cleaned_events.year,
        )

    delete cleaned_events.day
    delete cleaned_events.time_to
    delete cleaned_events.month
    delete cleaned_events.year

    cleaned_events = {
        ...cleaned_events,
        start_date: start_date,
        due_date: due_date
    }

    return cleaned_events
}
