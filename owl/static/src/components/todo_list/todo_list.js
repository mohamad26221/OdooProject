/** @odoo-module **/

import { registry } from '@web/core/registry';
const { Component ,useState} = owl;

export class OwlTodoList extends Component {
    setup(){
        this.state = useState({
        taskList:[
               {id:1, name:'Task 1', color:'#FF0000'},
               {id:2, name:'Task 2', color:'#000000'},
               {id:3, name:'Task 3', color:'#FFFFFF'},
        ]
        })
    }

}
OwlTodoList.template = 'owl.TodoList'
registry.category('actions').add('owl.action_todo_list_js', OwlTodoList);