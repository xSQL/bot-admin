import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

import { CrudAction, GroupItem } from '../../shared/types';
import { Config } from '../../config';


declare var $: any;
var cfg: Config = new Config();

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {

  private form: FormGroup;
  private action: CrudAction;
  private grouplist: GroupItem[];
  private item: GroupItem = new GroupItem();
  private community_id: string;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.form = new FormGroup({
      'community_id': new FormControl(null,[
        Validators.required
      ]),
      'name': new FormControl(null,[
        Validators.required
      ]),
    });

    this.action = new CrudAction()
    this.getList()
  }

  closeModal(element_id: string) {
    this.form.reset();
    $(`#${element_id}`).modal('hide');
  } 

  createAction() {
    this.action.title = 'Добавление сообщества';
    this.action.label = 'create';
    this.form.reset();
  }

  updateAction(id) {
    this.action.title = 'Редактирование сообщества';
    this.action.label = 'update';
    this.getItem(id).subscribe((response: GroupItem)=>{
      this.item = response;
      this.form.setValue({
        'name': response['name'],
        'community_id': response['community_id']
      });
    });
  }

  deleteAction(id) {
    this.action.title = 'Удалить сообщество';
    this.action.label = 'delete';
    this.getItem(id).subscribe((response: GroupItem)=>{
      this.item = response;
    });
  }

  getList() {
    let token = localStorage.getItem('jwt-token');
    this.http.get(`${cfg.server_url}/community/groups/`, {
      headers: {
        'Authorization': `JWT ${token}`
      }
    }).subscribe((response: GroupItem[])=>{
      this.grouplist = response;
    });
  }

  getItem(id) {
    let token = localStorage.getItem('jwt-token');
    return this.http.get(`${cfg.server_url}/community/group/${id}/`, {
      headers: {
        'Authorization': `JWT ${token}`
      }
    });
  }

  saveAction(element_id) {
    let token = localStorage.getItem('jwt-token');

    if(this.action.label=='create') {
      this.http.post(`${cfg.server_url}/community/groups/`, 
        this.form.value,
        {headers: {'Authorization': `JWT ${token}`}}
      ).subscribe(response=>{
        this.getList();
        this.closeModal(element_id);
      });
    } else if(this.action.label=='update') {
      this.http.put(`${cfg.server_url}/community/group/${this.item.pk}/`, 
        this.form.value,
        {headers: {'Authorization': `JWT ${token}`}}
      ).subscribe(response=>{
        this.getList();
        this.closeModal(element_id);
      });
    } else if(this.action.label=='delete') {
      this.http.delete(`${cfg.server_url}/community/group/${this.item.pk}/`, 
        {headers: {'Authorization': `JWT ${token}`}}
      ).subscribe(response=>{
        this.getList();
        this.closeModal(element_id);
      });
    }
  }

}
