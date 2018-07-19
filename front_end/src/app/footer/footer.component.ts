import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  name: string;
  plates: any;
  samples: any;
  subjects: any;

  constructor(private authService: AuthService) { }

  ngOnInit() {

    this.name = this.authService.getFullname();
    this.plates = 5;
    this.samples = 5;
    this.subjects = 5;

  }

}
