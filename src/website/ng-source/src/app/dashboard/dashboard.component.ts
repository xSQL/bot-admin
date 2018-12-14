import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { Config } from '../config';

let cfg: Config = new Config;

@Component({
  selector: 'bp-dashboard',
  templateUrl: './dashboard.component.html'
})
export class DashboardComponent {
  static_url = cfg.server_url+'/static/';

  constructor(private router: Router) {}

  logOut() {
    localStorage.setItem("jwt-token", '');
    console.log('logout');
    this.router.navigate(['/auth/login']);
  }

}
