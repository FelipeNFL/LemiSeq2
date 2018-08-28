import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UploadComponent } from '../upload/upload.component';
import { ChromPackService } from '../services/chrompack.service';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'subject-list',
  templateUrl: './subject-list.component.html',
  styleUrls: ['./subject-list.component.css']
})
export class SubjectListComponent implements OnInit {

  @Output() reset = new EventEmitter();
  @Output() viewSlots = new EventEmitter();
  chrompacks: Array<any>;
  selectedId: string;
  refreshMetricsSubscription: Subscription;

  constructor(private router: Router,
              private modalService: NgbModal,
              private chrompackService: ChromPackService,
              private chrompackServiceObservable: ChrompackServiceObservable) { }

  ngOnInit() {
    this.refreshMetricsSubscription = this.chrompackServiceObservable.getRefreshResult().subscribe(() => {
      this.getList();
    });

    this.getList();
  }

  refreshSelection(id) {
    this.chrompacks.forEach(chrompack => {

      if (chrompack._id === this.selectedId) {
        chrompack.selected = false;
      }

      if (chrompack._id === id) {
        chrompack.selected = true;
      }
    });
  } 

  select(id) {
    this.refreshSelection(id);
    this.selectedId = id;
    this.viewSlots.emit(id);
  }

  add() {
    this.modalService.open(UploadComponent);
  }

  getList() {
    this.chrompackService.getList().subscribe(result => {
      this.chrompacks = result;
    }, err => {
      //TODO exibir modal de erro
    });
  }

  delete() {
    this.chrompackService.delete(this.selectedId).subscribe(() => {
      this.getList();
      this.chrompackServiceObservable.sendRefreshResult();
    }, err => {
      //TODO exibir modal de erro
    });
  }

  back() {
    this.reset.emit();
  }
}
