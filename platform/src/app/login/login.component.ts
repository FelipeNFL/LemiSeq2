import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

// import { AuthService } from '../service/auth.service';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

    _usernameModel: string;
    _passwordModel: string;

    constructor(/*private authService: AuthService,*/
                private router: Router) { }
    
    ngOnInit(){
    }

    onSubmit(){

        // const authOjb = {username: this._usernameModel, password: this._passwordModel}

        // this.authService.login(authOjb).subscribe(
        //     (data) => { console.log(data); },
        //     (errorResponse: HttpErrorResponse) => { console.log(errorResponse); }
        // );
    }
}