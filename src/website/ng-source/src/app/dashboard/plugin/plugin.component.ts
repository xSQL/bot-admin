import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Config } from '../../config';

let cfg = new Config();

@Component({
  selector: 'app-plugin',
  templateUrl: './plugin.component.html',
  styleUrls: ['./plugin.component.css']
})
export class PluginComponent implements OnInit {

  private pluginlist: any;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    let token = localStorage.getItem('jwt-token');

    this.http.get(`${cfg.server_url}/community/extensions/`, {
      headers: {
        'Authorization': `JWT ${token}`
      }
    })
    .subscribe(response=>{
        this.pluginlist = response;
    })
  }

}
