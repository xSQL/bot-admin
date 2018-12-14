import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms'; 

import { UserService } from '../../shared/services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  private form: FormGroup;

  constructor(private user: UserService) { }

  ngOnInit() {
    this.form = new FormGroup({
      'email': new FormControl(
        null,
        [Validators.required, Validators.email]
      ),
      'password': new FormControl(
        null,
        [Validators.required, Validators.minLength(3)]
      )
    })
  }

  onSubmit() {
    this.user.login(this.form.value);
  }

}
