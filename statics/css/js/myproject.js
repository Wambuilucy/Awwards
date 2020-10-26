$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault()
        
        form = $("form")


        $.ajax({
            'url':'/ajax/ratings/{{project.id}}/',
            'type':'POST',
            'data':form.serialize(),
            'dataType':'json',
            'success':function(data){
                alert(data['success'])
                location.reload()
            },
        }) //End of Ajax
    }) //End of submit event
})//End of document ready function