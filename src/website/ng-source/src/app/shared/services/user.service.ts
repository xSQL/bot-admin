import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

import {Observable} from 'rxjs/Rx';
import "rxjs/add/operator/map"; 
import "rxjs/add/operator/catch"; 
import 'rxjs/add/observable/throw';

import { Config } from '../../config';

let cfg: Config = new Config();

class JwtResponse {
  public token: string;
}

@Injectable()
export class UserService {

  constructor(private http: HttpClient, private router: Router) {}

  login(data) {
    
    let formData: FormData = new FormData(); 
    formData.append('email', data['email']);
    formData.append('password', data['password']);

    this.http.post(cfg.server_url+'/jwt/obtain/', formData).subscribe((response: JwtResponse)=> {
      if(response.token) {
        localStorage.setItem('jwt-token', response.token);
        this.router.navigate(['/']);
      }
    })

  }

  verify() {
    let token = localStorage.getItem('jwt-token');
    
   if(token) {
      let formData: FormData = new FormData(); 
      formData.append('token', token);
      return this.http.post<boolean>(cfg.server_url+'/jwt/verify/', formData)
        .map((response)=> {
            return true;
        })
        .catch((error)=>{
            this.router.navigate(['/auth/login']);
            return  Observable.throw(error);
        });
      } else {
        this.router.navigate(['/auth/login']);
        return false;
      }
  }

}
