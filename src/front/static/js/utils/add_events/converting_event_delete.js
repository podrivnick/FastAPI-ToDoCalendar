async function converting_event_delete(
        events_obj,
        time = false
    )
{
    // clone object, which contains events data
    let cloneEventsArrForRequest = await JSON.parse(JSON.stringify(events_obj))
    // delete cloneEventsArrForRequest.events

    console.log(
        time['timeFrom'],
        time['timeTo'],
    )
    if (time) {
        cloneEventsArrForRequest['timeFrom'] = time['timeFrom'];
        cloneEventsArrForRequest['timeTo'] = time['timeTo'];
    }


    console.log(cloneEventsArrForRequest)
    // format time to ISO format
    const start_date = await
        formatDateTime
        (
            cloneEventsArrForRequest.day,
            cloneEventsArrForRequest.timeFrom,
            cloneEventsArrForRequest.month,
            cloneEventsArrForRequest.year,
        )
    const due_date = await
        formatDateTime
        (
            cloneEventsArrForRequest.day,
            cloneEventsArrForRequest.timeTo,
            cloneEventsArrForRequest.month,
            cloneEventsArrForRequest.year,
        )


    delete cloneEventsArrForRequest.day
    delete cloneEventsArrForRequest.timeTo
    delete cloneEventsArrForRequest.timeFrom
    delete cloneEventsArrForRequest.month
    delete cloneEventsArrForRequest.year

    cloneEventsArrForRequest = {
        ...cloneEventsArrForRequest,
        start_date: start_date,
        due_date: due_date
    }

    return JSON.stringify(cloneEventsArrForRequest)
}
