async function converting_event_delete(
        events_obj
    )
{
    // clone object, which contains events data
    let cloneEventsArrForRequest = await JSON.parse(JSON.stringify(events_obj))
    delete cloneEventsArrForRequest.events

    // format time to ISO format
    const start_date = await
        formatDateTime
        (
            cloneEventsArrForRequest.day,
            cloneEventsArrForRequest.time_from,
            cloneEventsArrForRequest.month,
            cloneEventsArrForRequest.year,
        )
    const due_date = await
        formatDateTime
        (
            cloneEventsArrForRequest.day,
            cloneEventsArrForRequest.time_to,
            cloneEventsArrForRequest.month,
            cloneEventsArrForRequest.year,
        )


    delete cloneEventsArrForRequest.day
    delete cloneEventsArrForRequest.time_to
    delete cloneEventsArrForRequest.time_from
    delete cloneEventsArrForRequest.month
    delete cloneEventsArrForRequest.year

    cloneEventsArrForRequest = {
        ...cloneEventsArrForRequest,
        start_date: start_date,
        due_date: due_date
    }

    return JSON.stringify(cloneEventsArrForRequest)
}
