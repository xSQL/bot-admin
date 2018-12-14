import { Component } from '@angular/core';
import { Config } from './config';

let cfg = new Config();

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: [
    './app.component.css'
  ]
})
export class AppComponent {
  title = 'app';
  static_url = cfg.server_url+'/static/';
}
