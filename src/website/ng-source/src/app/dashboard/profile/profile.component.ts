import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

import { UserItem } from '../../shared/types';
import { Config } from '../../config';

var cfg: Config = new Config();

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  private form: FormGroup;
  private token: string;


  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.token = localStorage.getItem('jwt-token');
    this.http.get(`${cfg.server_url}/accounts/user/self/`, {
      headers: {
        'Authorization': `JWT ${this.token}`
      }
    }).subscribe((response: UserItem)=>{
      this.form.setValue(response);
    });

    this.form = new FormGroup({
      'first_name': new FormControl(null, []),
      'middle_name': new FormControl(null, []),
      'last_name': new FormControl(null, []),
      'phone': new FormControl(null, []),
      'skype': new FormControl(null, []),
      'telegram': new FormControl(null, []),
    });
  }

  saveAction() {
    this.http.put(`${cfg.server_url}/accounts/user/self/`, 
      this.form.value,
      {headers: {'Authorization': `JWT ${this.token}`}}
    ).subscribe((response: UserItem)=>{
      this.form.setValue(response);
    });
  }

}
