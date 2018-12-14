import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

import { CrudAction, GroupItem, SynonymItem, SynonymPagination } from '../../shared/types';
import { Config } from '../../config';


declare var $: any;
var cfg: Config = new Config();


@Component({
  selector: 'app-synonym',
  templateUrl: './synonym.component.html',
  styleUrls: ['./synonym.component.css']
})
export class SynonymComponent implements OnInit {

  private form: FormGroup;
  private action: CrudAction;
  private token: string;
  private groups: GroupItem[];
  private synonyms: SynonymItem[];
  private item: SynonymItem;
  private nextLink: string;
  private prevLink: string;
  private lastLink: string;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.token = localStorage.getItem('jwt-token');
    this.http.get(`${cfg.server_url}/community/groups/`, {
      headers: {
        'Authorization': `JWT ${this.token}`
      }
    }).subscribe((response: GroupItem[])=>{
      this.groups = response;
    });
    this.form = new FormGroup({
      'name': new FormControl(null, [Validators.required]),
      'text': new FormControl(null, [Validators.required]),
      'community': new FormControl(null, [Validators.required])
    });
    this.action = new CrudAction();
    this.getList()
  }

  getList() {
    if(!this.lastLink) 
      this.lastLink = `${cfg.server_url}/community/synonyms/`;
    this.getListByUrl(this.lastLink);
  }

  getListByUrl(url) {
    this.lastLink = url;
    this.http.get(url, {
      headers: {
        'Authorization': `JWT ${this.token}`
      }
    }).subscribe((response: SynonymPagination)=>{
      this.synonyms = response.results;
      this.nextLink = response.next;
      this.prevLink = response.previous;
    });
  }

  getNext() {
    this.getListByUrl(this.nextLink);
  }

  getPrev() {
    this.getListByUrl(this.prevLink);
  }

  getItem(id) {
    let token = localStorage.getItem('jwt-token');
    return this.http.get(`${cfg.server_url}/community/synonym/${id}/`, {
      headers: {
        'Authorization': `JWT ${token}`
      }
    });
  }

  createAction() {
    this.action.title = 'Добавление синонима';
    this.action.label = 'create';
  }
    
  updateAction(id) {
    this.action.title = 'Редактирование синонима';
    this.action.label = 'update';
    this.getItem(id).subscribe((response: SynonymItem)=>{
      this.item = response;
      this.form.setValue({
        'name': response['name'],
        'text': response['text'],
        'community': response['community']
      });
    });
  }

  deleteAction(id) {
    this.action.title = 'Удалить синоним';
    this.action.label = 'delete';
    this.getItem(id).subscribe((response: SynonymItem)=>{
      this.item = response;
    });
  }

  closeModal(element_id: string) {
    this.form.reset();
    $(`#${element_id}`).modal('hide');
  } 


  saveAction(element_id='modal') {
    if(this.action.label=='create') {
      this.http.post(`${cfg.server_url}/community/synonyms/`, 
        this.form.value,
        {headers: {'Authorization': `JWT ${this.token}`}}
      ).subscribe(response=>{
        this.getList();
        this.closeModal(element_id);
      });
    } else if(this.action.label=='update') {
      this.http.put(`${cfg.server_url}/community/synonym/${this.item.pk}/`, 
        this.form.value,
        {headers: {'Authorization': `JWT ${this.token}`}}
      ).subscribe(response=>{
        this.getList();
        this.closeModal(element_id);
      });
    } else if(this.action.label=='delete') {
      this.http.delete(`${cfg.server_url}/community/synonym/${this.item.pk}/`, 
        {headers: {'Authorization': `JWT ${this.token}`}}
      ).subscribe(response=>{
        this.getList();
        this.closeModal(element_id);
      });
    }
  }
}
