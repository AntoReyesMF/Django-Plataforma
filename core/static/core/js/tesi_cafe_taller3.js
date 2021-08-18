$( function(){
  'use strict';

  var models = {
      notes : [],
      createLocalStorage : function(){
        // create local storage if no local storage exists with welcome message
          models.notes.push({noteContent : 'Puedes escribir y crear más notas',x:0,y:0});
         models.setLocalStorage(models.notes);
      },
      setLocalStorage : function(value) {
          localStorage.setItem('notes',JSON.stringify(value));
      },
      getLocalStorage : function(){
        return JSON.parse(localStorage.notes);
      }
  }

  var views = {
      createEl : function(element,classname){
        // create element dynamically..
        var el = document.createElement(element);
           el.className = classname || '';
           return el;
      },
      displayNotes : function(notes){
        // display Notes based on the length of Localstorage value
       var container = document.querySelector('.teca_tesis_taller3_notas') 
        notes = JSON.parse(notes);
        notes.forEach(function(element,index) {
            var note = views.createEl('div','teca_tesis_taller3_note'),
                note_header = views.createEl('div','teca_tesis_taller3_note_header'),
               notecontent = views.createEl('textarea','textareacontent'),
               addBtn = views.createEl('button','addBtn'),
               closeBtn = views.createEl('button','closeBtn');
               addBtn.textContent = "+";
               closeBtn.textContent = "x";
               note.id = index;
               notecontent.textContent = element.noteContent;
               note_header.appendChild(addBtn);
               note_header.appendChild(closeBtn);
               note_header.appendChild(notecontent);
               note.appendChild(note_header);
               // set note view left and top from localstorage x and y properties.
               note.style.left = element.x + 'px';   
               note.style.top = element.y + 'px';
               container.appendChild(note);
        }, this);
        
      },
      clearNotesView : function(){
        // clear all the notes 
           var container = document.querySelector('.teca_tesis_taller3_notas') 
               while(container.firstChild){
                   container.removeChild(container.firstChild);
               }
      },
      dragNote : function(){
        // Jquery Draggable
        var index;
           $('.teca_tesis_taller3_note').draggable({
            drag : function(event,ui){
               var notes = models.getLocalStorage();
                 index = event.target.id;
                 views.frontNote(index);
                 // set update left and top value of note back to local storage
                 notes[event.target.id].x = ui.position.left;
                 notes[event.target.id].y = ui.position.top;
                 models.setLocalStorage(notes);
            }
          });
      },
      frontNote : function(id){
        // toggle z-index value to make working note on top of others..
        id = id * 1;
        var notes = document.querySelectorAll('.teca_tesis_taller3_note.ui-draggable.ui-draggable-handle');
            notes.forEach(function(item,index){
                if(index === id){
                  item.style.zIndex = "1";
                }
                else {
                  item.style.zIndex = "0";
                }
            },this);
      },
      init : function(){
        // all view events
       var container = document.querySelector('.teca_tesis_taller3_notas');
           container.addEventListener('click',function(e){
               var classname = e.target.className;
                if(classname === "addBtn"){
                   controller.addNote();
                } else if(classname === "closeBtn") { 
                   controller.closeNote(e.target.parentElement.parentElement.id);
                } else if(classname === "teca_tesis_taller3_note_header" || classname === "textareacontent"){
                  var noteContainer = e.target.parentElement.className === "teca_tesis_taller3_note ui-draggable ui-draggable-handle" ?  e.target.parentElement : e.target.parentElement.parentElement;
                     views.frontNote(noteContainer.id);
                }
                
                views.dragNote();
           })
           container.addEventListener('keyup',function(e){
             if(e.target.className === "textareacontent"){
               controller.storeNoteContent(e.target.parentElement.parentElement.id,e.target.value);
             }
           })
      }
  }

  var controller = {
     localStorageExistance : function(){
       // Check if the Local Storage existance in browser (notes)
       if(localStorage.notes === undefined || JSON.parse(localStorage.notes).length === 0){
           models.createLocalStorage();  // create local storage
           views.displayNotes(localStorage.notes); 
       } else {
           views.displayNotes(localStorage.notes);
       }
     },
     addNote : function(){
       // add note
        models.notes = models.getLocalStorage();
        var l = models.notes.length;
        models.notes.push({noteContent: '',x:30 * l,y:30*l});
        models.setLocalStorage(models.notes);
        views.clearNotesView();
        views.displayNotes(localStorage.notes);
     },
     closeNote : function(id){
       // close note
        id = id * 1;
        var notes = models.getLocalStorage();
        notes.splice(id,1);
        models.setLocalStorage(notes);
        views.clearNotesView();
        views.displayNotes(localStorage.notes);
     },
     storeNoteContent : function(id,value){
       // store note content back to local storage...
       id = id * 1;
       var notes = models.getLocalStorage();
           notes[id].noteContent = value;
           models.setLocalStorage(notes);
     },
      init : function(){
          controller.localStorageExistance();   
          views.init();
      }
  }
  controller.init();   // App initial Call
  views.dragNote();  // Note draggable 
 
})