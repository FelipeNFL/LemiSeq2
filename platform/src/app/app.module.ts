import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app-component/app.component';
import { HeaderComponent } from './header/header.component' 
import { RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { UploadComponent } from './upload/upload.component';

import { ChromPackService } from '../services/chrompack.service';

import { appRoutes } from './routes';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LoginComponent,
    UploadComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot(appRoutes)
  ],
  bootstrap: [AppComponent],
  providers: [
    ChromPackService,
  ]
})
export class AppModule { }
